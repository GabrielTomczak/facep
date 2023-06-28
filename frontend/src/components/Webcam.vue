<template>
  <div>
    <video ref="videoElement" autoplay></video>
    <button class="btn btn-success" @click="capture"><img src="../assets/camera-fill.svg" class="bi bi-camera-fill"></button>
    {{ faceData }}
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      videoElement: null,
      faceData: {}
    };
  },
  mounted() {
    this.initializeCamera();
  },
  methods: {
    async initializeCamera() {
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        try {
          const stream = await navigator.mediaDevices.getUserMedia({ video: true });
          console.log(stream)
          this.videoElement = stream;
          this.$refs.videoElement.srcObject = stream;
          this.$refs.videoElement.play();
        } catch (error) {
          console.error('Erro ao acessar a webcam:', error);
        }
      }
    },
    capture() {
      const canvas = document.createElement('canvas');
      canvas.width = this.$refs.videoElement.videoWidth;
      canvas.height = this.$refs.videoElement.videoHeight;
      const context = canvas.getContext('2d');
      context.drawImage(
        this.$refs.videoElement,
        0,
        0,
        canvas.width,
        canvas.height
      );

      const dataURI = canvas.toDataURL('image/png');

      const link = document.createElement('a');
      link.href = dataURI;
      link.download = 'face.png';
      link.click();

      axios.get('http://127.0.0.1:5000/face_analysis')
        .then(response => {
          this.faceData = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    cleanup() {
      if (this.videoElement) {
        this.videoElement.getTracks().forEach(track => track.stop());
      }
    }
  },
  beforeUnmount() {
    this.cleanup();
  }
};
</script>
