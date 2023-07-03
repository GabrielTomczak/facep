<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      videoElement: null,
      faceData: {},
      faceHeight: "",
      faceWidth: "",
      upperThird: "",
      middleThird: "",
      lowerThird: "",
      faceHeightDesc: "",
      faceWidthDesc: "",
      upperThirdDesc: "",
      middleThirdsDesc: "",
      lowerThirdDesc: "",
    };
  },
  mounted() {
    this.startCamera();
  },
  methods: {
    async startCamera() {
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        try {
          const stream = await navigator.mediaDevices.getUserMedia({ video: true });
          this.videoElement = stream;
          this.$refs.videoElement.srcObject = stream;
          this.$refs.videoElement.play();
        } catch (error) {
          console.error('Erro ao acessar a webcam:', error);
        }
      }
    },
    takePhoto() {
      this.faceData = {}
      const canvas = document.createElement('canvas');
      // canvas.width = this.$refs.videoElement.videoWidth;
      // canvas.height = this.$refs.videoElement.videoHeight;
      canvas.width = 1280;
      canvas.height = 720;
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
          this.faceHeight = this.faceData["Trme_zizi"];
          this.faceWidth = this.faceData["Zizi_Gogo"];
          this.upperThird = this.faceData["terco_superior"];
          this.middleThird = this.faceData["terco_meio"];
          this.lowerThird = this.faceData["terco_inferior"];
          this.faceHeightDesc = this.faceData["Trme_zizi_desc"];
          this.faceWidthDesc = this.faceData["Zizi_Gogo_desc"];
          this.upperThirdDesc = this.faceData["terco_superior_desc"];
          this.middleThirdsDesc = this.faceData["terco_meio_desc"];
          this.lowerThirdDesc = this.faceData["terco_inferior_desc"];
          this.$emit('facedata', this.faceData);
        })
        .catch(error => {
          console.error(error);
        });
    },
    clearCamera() {
      if (this.videoElement) {
        this.videoElement.getTracks().forEach(track => track.stop());
      }
    }
  },
  beforeUnmount() {
    this.clearCamera();
  }
};
</script>
<template>
  <div class="info">
    <p>Encaixe o rosto dentro do molde para tirar a foto.</p>
  </div>
  <div class="webcam">
    <div class="video-container">
      <video ref="videoElement" autoplay></video>
      <div class="image-overlay">
        <img src="../assets/face.png">
      </div>
    </div>
    <div class="camera">
      <table class="table table-dark">
        <thead>
          <tr>
            <th scope="col">Altura da Face</th>
            <th scope="col">Largura da face</th>
            <th scope="col">Terço Superior</th>
            <th scope="col">Terço Médio</th>
            <th scope="col">Terço Inferior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">{{ faceHeight }}</th>
            <td>{{ faceWidth }}</td>
            <td>{{ upperThird }}</td>
            <td>{{ middleThird }}</td>
            <td>{{ lowerThird }}</td>
          </tr>
        </tbody>
      </table>
      <table class="table table-dark">
        <tbody>
          <tr>
            <th scope="row">{{ faceHeightDesc }}</th>
          </tr>
        </tbody>
      </table>
      <table class="table table-dark">
        <tbody>
          <tr>
            <th scope="row">{{ faceWidthDesc }}</th>
          </tr>
        </tbody>
      </table>
      <table class="table table-dark">
        <tbody>
          <tr>
            <th scope="row">{{ upperThirdDesc }}</th>
          </tr>
        </tbody>
      </table>
      <table class="table table-dark">
        <tbody>
          <tr>
            <th scope="row">{{ middleThirdsDesc }}</th>
          </tr>
        </tbody>
      </table>
      <table class="table table-dark">
        <tbody>
          <tr>
            <th scope="row">{{ lowerThirdDesc }}</th>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="btn">
    <button class="btn btn-success" @click="takePhoto"><img src="../assets/camera-fill.svg" class="bi bi-camera-fill"></button>
  </div>
</template>

<style>
.video-container {
  position: relative;
  width: 640px;
}
.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
.info {
  display: flex;
  margin-top: 10px;
}
.image-overlay img {
  width: 100%;
  height: 100%;
  opacity: 50%;
  object-fit: cover;
}
.webcam {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}
.camera table{
  justify-content: center;
  margin-left: 100px;
}
.btn button {
  margin-top: 20px;
  width: 80px;
  height: 80px;
  border-radius: 100px;
}
</style>
