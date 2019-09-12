<template>
  <div class=main>
    <button v-on:click.stop="scroll('#about-page')">About</button>
    <button v-on:click.stop="scroll('#station-page')">Station</button>
    <button v-on:click.stop="scroll('#schedule-page')">Schedule</button>
  </div>
</template>

<script>
export default {
  name: "TabBar",
  methods: {
    scroll: function (target) {
      var self = this;
      this.$emit("toggleSnap", false);

      this.$scrollTo(target, 500, {
        container: "#slider",
        easing: "ease",
        cancelable: true,
        y: false,
        x: true,

        onDone: function(element) {
          self.$emit("toggleSnap", true)},

        onCancel: function() {
          self.$emit("toggleSnap", true)}
      });
    }}
};
</script>

<style scoped>
p {
  text-align: center;
}

button {
    width: 33.3%;
    font-family: "Montserrat", sans-serif;
    color: #F8F8F8;
    font-weight: 500;
    font-size: 15px;
    height: 100%;
    border: none;
    background-color: Transparent;
    text-align: center;
    text-decoration: none;
    outline: none;
}

.main {
  background-color: Transparent;
  height: 50px;
  width: 80vw;
  position: relative;
  z-index: 1;
  bottom: 10vh;
  margin: 0 auto;
}
</style>
