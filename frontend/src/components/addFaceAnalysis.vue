<script>
import TextInput from './TextInput.vue';
import TextArea from './TextArea.vue';
import Webcam from './Webcam.vue';
import axios from 'axios';
export default {
  components: {
    TextInput,
    TextArea,
    Webcam
  }
}
</script>

<template>
  <header>
    <h1>Face.p</h1>
  </header>
  <div class="main">
    <div class="input">
      <TextInput msg="Nome do Perfil"/>
    </div>
    <div class="camera">
      <Webcam ref="cam" />
    </div>
    <div v-if="showBtns" class="action-buttons">
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

#saveAnalysis {
  margin-right: 10px;
}
@media (min-width: 1024px) {

}
</style>
