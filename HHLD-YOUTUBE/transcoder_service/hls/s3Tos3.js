import dotenv from "dotenv";
import AWS from 'aws-sdk';
import fs from "fs";
import ffmpegStatic from "ffmpeg-static"
const s3 = new AWS.S3({
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
 });
  const s3tos3 = async()=>{
    console.log('Starting script');
    console.time('req_time');
    try {
        console.log('Downloading s3 mp4 file locally');
        const mp4FilePath = `${mp4FileName}`;
        const writeStream = fs.createWriteStream('local.mp4');
        const readStream = s3
            .getObject({ Bucket: bucketName, Key: mp4FilePath })
            .createReadStream();
        readStream.pipe(writeStream);
        await new Promise((resolve, reject) => {
            writeStream.on('finish', resolve);
            writeStream.on('error', reject);
        });
        console.log('Downloaded s3 mp4 file locally');
        const resolutions = [
            {
                resolution: '320x180',
                videoBitrate: '500k',
                audioBitrate: '64k'
            },
            {
                resolution: '854x480',
                videoBitrate: '1000k',
                audioBitrate: '128k'
            },
            {
                resolution: '1280x720',
                videoBitrate: '2500k',
                audioBitrate: '192k'
            }
        ];
  const variantPlaylists=[];// to see how  many variant playlist can be there
  for (const { resolution, videoBitrate, audioBitrate } of resolutions) {
    console.log(`HLS conversion starting for ${resolution}`);
           const outputFileName = `${mp4FileName.replace(
               '.',
               '_'
           )}_${resolution}.m3u8`;
           const segmentFileName = `${mp4FileName.replace(
            '.',
            '_'
        )}_${resolution}_%03d.ts`;
        await new Promise((resolve, reject) => {
            ffmpeg('./local.mp4')
                .outputOptions([
                    `-c:v h264`,
                    `-b:v ${videoBitrate}`,
                    `-c:a aac`,
                    `-b:a ${audioBitrate}`,
                    `-vf scale=${resolution}`,
                    `-f hls`,
                    `-hls_time 10`,
                    `-hls_list_size 0`,
                    `-hls_segment_filename hls/${segmentFileName}`
                ])
                .output(`hls/${outputFileName}`)
                .on('end', () => resolve())
                .on('error', (err) => reject(err))
                .run();
        });
        const variantPlaylist = {
            resolution,
            outputFileName
        };
        variantPlaylists.push(variantPlaylist);
        console.log(`HLS conversion done for ${resolution}`);
    }
    console.log(`HLS master m3u8 playlist generating`);
    let masterPlaylist = variantPlaylists
        .map((variantPlaylist) => {
            const { resolution, outputFileName } = variantPlaylist;
            const bandwidth =
                resolution === '320x180'
                    ? 676800
                    : resolution === '854x480'
                    ? 1353600
                    : 3230400;
            return `#EXT-X-STREAM-INF:BANDWIDTH=${bandwidth},RESOLUTION=${resolution}\n${outputFileName}`;
        })
        .join('\n');
//         The original filename (mp4FileName) is likely an MP4 video file.
// The code is creating a new filename for the master playlist, which is a file that contains information about all the available video qualities and their locations.
// The transformation happens as follows:
// a. mp4FileName.replace('.', '_'): This replaces the dot in the original filename with an underscore. This is likely done to avoid having multiple dots in the filename, which could cause issues with file extensions.
// b. _master is appended to indicate that this is the master playlist file.
// c. .m3u8 is the standard file extension for HLS playlist files.

// The result is a new filename that clearly relates to the original video file, indicates it's a master playlist, and has the correct extension for HLS.
// For example, if mp4FileName was "video.mp4", the resulting masterPlaylistFileName would be "video_mp4_master.m3u8".
    masterPlaylist = `#EXTM3U\n` + masterPlaylist;
    const masterPlaylistFileName = `${mp4FileName.replace(
        '.',
        '_'
    )}_master.m3u8`;
    const masterPlaylistPath = `hls/${masterPlaylistFileName}`;
    fs.writeFileSync(masterPlaylistPath, masterPlaylist);
    console.log(`HLS master m3u8 playlist generated`);
    console.log(`Deleting locally downloaded s3 mp4 file`);


    fs.unlinkSync('local.mp4');
    console.log(`Deleted locally downloaded s3 mp4 file`);
    console.log(`Uploading media m3u8 playlists and ts segments to s3`);

    const files = fs.readdirSync(hlsFolder);
    for (const file of files) {
        if (!file.startsWith(mp4FileName.replace('.', '_'))) {
            continue;
        }
        const filePath = path.join(hlsFolder, file);
        const fileStream = fs.createReadStream(filePath);
        const uploadParams = {
            Bucket: bucketName,
            Key: `${hlsFolder}/${file}`,
            Body: fileStream,
            ContentType: file.endsWith('.ts')
                ? 'video/mp2t'
                : file.endsWith('.m3u8')
                ? 'application/x-mpegURL'
                : null
        };
        await s3.upload(uploadParams).promise();
        fs.unlinkSync(filePath);
    }
    console.log(
        `Uploaded media m3u8 playlists and ts segments to s3. Also deleted locally`
    );

       const files = fs.readdirSync(hlsFolder);
       for (const file of files) {
           if (!file.startsWith(mp4FileName.replace('.', '_'))) {
               continue;
           }
           const filePath = path.join(hlsFolder, file);
           const fileStream = fs.createReadStream(filePath);
           const uploadParams = {
               Bucket: bucketName,
               Key: `${hlsFolder}/${file}`,
               Body: fileStream,
               ContentType: file.endsWith('.ts')
                   ? 'video/mp2t'
                   : file.endsWith('.m3u8')
                   ? 'application/x-mpegURL'
                   : null
           };
           await s3.upload(uploadParams).promise();
           fs.unlinkSync(filePath);
       }
       console.log(
           `Uploaded media m3u8 playlists and ts segments to s3. Also deleted locally`
       );


    }