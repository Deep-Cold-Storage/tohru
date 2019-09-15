<template>
  <div>
    <AboutPageInfo/>
    <AboutPageOptions v-on:setSmartRoute="setSmartRoute" v-bind:useSmartRoute="useSmartRoute" />
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
    useSmartRoute: Boolean,
  },

  methods: {
    setSmartRoute: function(boolean) {
      this.$emit("setSmartRoute", boolean);
    },
  }
};
</script>
