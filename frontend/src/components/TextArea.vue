<script>
export default {
  props: {
    label: String
  }
}
</script>

<template>
  <div class="text-label">
    <!-- <label for="description">{{ label }}</label> -->
  </div>
  <textarea name="description" placeholder="Observações do Profissional" cols="100" rows="10" style="resize:none"></textarea>
</template>

<style>
  .text-label {
    display: flex;
    flex-direction: column;
  }
  textarea {
    border-radius: 6px;
  }
</style>