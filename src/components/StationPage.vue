<template>
  <div>
    <StationPageRoute v-bind:route="route"/>
    <StationPageLive v-bind:route="route"/>
  </div>
</template>

<script>
import StationPageRoute from "./StationPageRoute.vue";
import StationPageLive from "./StationPageLive.vue";

export default {
  name: "StationPage",
  components: {
    StationPageRoute,
    StationPageLive
  },
  props: {
    route: Object
  }
};
</script>

<style scoped>
</style>
