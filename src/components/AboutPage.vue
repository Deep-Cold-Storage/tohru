<template>
  <div>
    <AboutPageInfo />
    <AboutPageOptions v-bind:useGPS="useGPS" />
  </div>
</template>

<script>
import AboutPageInfo from "./AboutPageInfo.vue";
import AboutPageOptions from "./AboutPageOptions.vue";

export default {
  name: "AboutPage",
  components: {
    AboutPageInfo,
    AboutPageOptions
  },
  props: {
    useGPS: Boolean
  }
};
</script>
