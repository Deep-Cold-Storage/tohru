<template>
  <div class="about-page">
    <AboutPageInfo/>
  </div>
</template>

<script>
import AboutPageInfo from "./AboutPageInfo.vue";

export default {
  name: "AboutPage",
  components: {
    AboutPageInfo
  },
  props: {
    msg: String
  }
};
</script>

<style scoped>
</style>
