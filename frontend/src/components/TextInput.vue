<script>
export default{
  data() {
    return {
      name: "",
    }
  },
  props: {
    msg: String,
    modelValue: String,
  }
}
</script>
<template>
  <div class="input-label">
    <label>{{ msg }}</label>
  </div>
  <input :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" type="text" class="form-control">
</template>

<style>
.input-label label{
  display: flex;
  flex-direction: initial;
}
input {
  max-width: 500px;
}
</style>