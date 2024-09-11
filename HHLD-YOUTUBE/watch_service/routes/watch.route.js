import express from "express"
import watchVideo from "../controllers/watch.controller.js";
import getAllVideos from "../controllers/home.controller.js";

const router = express.Router();

router.get('/', watchVideo);
router.get('/home', getAllVideos);

export default router;// This is your Prisma schema file,
// learn more about it in the docs: https://pris.ly/d/prisma-schema

// Looking for ways to speed up your queries, or scale easily with your serverless or edge functions?
// Try Prisma Accelerate: https://pris.ly/cli/accelerate-init