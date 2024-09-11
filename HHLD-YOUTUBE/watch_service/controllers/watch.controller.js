import AWS from "aws-sdk"

async function generateSignedUrl(videoKey) {

   const s3 = new AWS.S3({
       accessKeyId: process.env.AWS_ACCESS_KEY_ID,
       secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
       region: 'ap-south-1'
   });

   const params = {
       Bucket: process.env.AWS_BUCKET,
       Key: videoKey,
       Expires: 3600 // URL expires in 1 hour, adjust as needed
   };

   return new Promise((resolve, reject) => {
       s3.getSignedUrl('getObject', params, (err, url) => {
           if (err) {
               reject(err);
           } else {
               resolve(url);
           }
       });
   });
}