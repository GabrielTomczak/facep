<script>
export default{
  props: {
    msg: String
  }
}
</script>
<template>
  <div class="input-label">
    <label>{{ msg }}</label>
  </div>
  <input type="text" class="form-control">
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