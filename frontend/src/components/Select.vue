<script>
export default{
  data() {
    return {
      sex: "",
    }
  },
  props: {
    msg: String,
    modelValue: String
  }
}
</script>
<template>
  <div class="select-label">
    <label>{{ msg }}</label>
  </div>
  <select :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" class="form-select">
    <option value="male">Homem</option>
    <option value="female">Mulher</option>
  </select>
</template>

<style>
.select-label label{
  margin-top: 20px;
  display: flex;
  flex-direction: initial;
}
select {
  max-width: 200px;
}
</style>