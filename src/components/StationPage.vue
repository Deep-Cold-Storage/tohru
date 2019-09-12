<template>
  <div class="page">
    <p>Station!</p>
    <p>{{ data }}</p>
  </div>
</template>

<script>
export default {
  name: "StationPage",
  props: {
    data: String
  }
};
</script>

<style scoped>
p {
  font-family: "Montserrat", sans-serif;
  text-align: center;
  color: #f8f8f8;
}
</style>
