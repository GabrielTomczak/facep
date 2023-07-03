<script>
import TextInput from './TextInput.vue';
import TextArea from './TextArea.vue';
import Select from './Select.vue';
import Webcam from './Webcam.vue';
import axios from 'axios';
export default {
  components: {
    TextInput,
    TextArea,
    Select,
    Webcam
  },
  data(){
    faceData: {};
  },
  methods: {
    getData(value) {
      this.faceData = value;
    }
  }
}
</script>

<template>
  <header>
    <h1>Face.p</h1>
  </header>
  <div class="main">
    <form class="input">
      <TextInput msg="Nome do Paciente"/>
      <Select msg="sexo"/>
    </form>
    <div class="camera">
      <Webcam ref="cam" @facedata="getData" />
    </div>
    <div class="results">
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
