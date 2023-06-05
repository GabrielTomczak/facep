<script>
import TextInput from './TextInput.vue';
import Camera from 'simple-vue-camera';
import TextArea from './TextArea.vue';
import axios from 'axios';
import { WebCam } from 'vue-camera-lib'
export default {
  components: {
    TextInput,
    Camera,
    TextArea,
    WebCam
  },
  methods: {
    takePicture() {
      this.$refs.webcam.takePhoto();
      this.$emit.webcam.stop();

      axios.get('http://127.0.0.1:5000/face_analysis')
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.error(error);
      });
    },
  }
}

</script>

<template>
  <header>
    <h1>Análise Facial</h1>
  </header>
  <div class="main">
    <TextInput msg="Nome do Perfil"/>
    <div class="camera">
      <WebCam ref="webcam" :audio="false" :shutterEffect="false"/>
      <button class="btn btn-success" @click="takePicture()">Tira foto</button>
    </div>
    <div class="description">
      <TextArea label="Observações do Profissional"></TextArea>
    </div>
    <div class="action-buttons">
      <button id="saveAnalysis" class="btn btn-success">Salvar</button>
      <button id="cancelAnalysis" class="btn btn-danger">Cancelar</button>
    </div>
  </div>
</template>

<style scoped>
header {
  color: white;
  font-weight: bold;
  margin: 10px;
}
.main{
  padding-top: 30px;
  color: white;
  text-align: center;
  margin: 10px;
}

.camera {
  margin-top: 50px;
  max-width: 500px;
  max-height: 500px;
}
.camera button {
  margin-top: 10px;
}
.description {
  display: flex;
  margin-top: 20px;
}
.action-buttons {
  margin-top: 20px;
  display: flex;
}
#saveAnalysis {
  margin-right: 10px;
}
@media (min-width: 1024px) {

}
</style>
