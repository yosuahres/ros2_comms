<template>
  <div>
    <h1>ROS Image Stream</h1>
    <img :src="imageSrc" alt="ROS Image Stream" />
  </div>
</template>

<script>
import ROSLIB from 'roslib';

export default {
  data() {
    return {
      ros: null,
      imageSrc: '',
    };
  },
  mounted() {
    this.connectToRos();
  },
  methods: {
    connectToRos() {
      this.ros = new ROSLIB.Ros({
        url: 'ws://localhost:9090', // Adjust the URL if needed
      });

      this.ros.on('connection', () => {
        console.log('Connected to websocket server.');
        this.subscribeToImageTopic();
      });

      this.ros.on('error', (error) => {
        console.log('Error connecting to websocket server: ', error);
      });

      this.ros.on('close', () => {
        console.log('Connection to websocket server closed.');
      });
    },
    subscribeToImageTopic() {
      const imageTopic = new ROSLIB.Topic({
        ros: this.ros,
        name: '/image_frame',
        messageType: 'sensor_msgs/Image',
      });

      imageTopic.subscribe((message) => {
        this.imageSrc = 'data:image/jpeg;base64,' + message.data;
      });
    },
  },
};
</script>

<style scoped>
img {
  max-width: 100%;
  height: auto;
}
</style>
