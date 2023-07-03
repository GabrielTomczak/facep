<script>
export default{
  props: {
    msg: String
  }
}
</script>
<template>
  <div class="select-label">
    <label>{{ msg }}</label>
  </div>
  <select class="form-select">
    <option value="1">Homem</option>
    <option value="2">Mulher</option>
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