<template>
  <div>
    <StationPageRoute
      v-on:toggleSelectPage="toggleSelectPage"
      v-on:setRoute="setRoute"
      v-bind:route="route"
    />
    <StationPageLive v-bind:route="route" />
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
  },
  methods: {
    setRoute: function(data) {
      this.$emit("setRoute", data);
    },

    toggleSelectPage: function() {
      this.$emit("toggleSelectPage");
    }
  }
};
</script>

<style scoped></style>
