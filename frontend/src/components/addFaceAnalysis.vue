<script>
import TextInput from './TextInput.vue';
import TextArea from './TextArea.vue';
import Select from './Select.vue';
import Webcam from './Webcam.vue';
export default {
  components: {
    TextInput,
    TextArea,
    Select,
    Webcam
  },
  data(){
    return {
      faceData: {},
      name: "",
      sex: "",
      value: "",
    }
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
    <div class="input">
      <TextInput v-model="name" v-model:name="name" msg="Nome do Paciente"/>
      <Select v-model="sex" v-model:sex="sex" msg="sexo"/>
    </div>
    <div class="camera">
      <Webcam :name="name" :sex="sex" ref="cam" @facedata="getData" />
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
