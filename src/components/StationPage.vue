<template>
  <div class="station-page">
    <Route></Route>
    <StationLive></StationLive>
  </div>
</template>

<script>
import Route from "./Route.vue";
import StationLive from "./StationLive.vue";

export default {
  name: "StationPage",
  components: {
    Route,
    StationLive
  },
};
</script>

<style scoped>
p {
  text-align: center;
}
</style>
