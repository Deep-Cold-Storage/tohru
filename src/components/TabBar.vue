<template>
  <div class=main>
    <button v-on:click.stop="scroll('AboutPage')">About</button>
    <button v-on:click.stop="scroll('StationPage')">Station</button>
    <button v-on:click.stop="scroll('SchedulePage')">Schedule</button>
  </div>
</template>

<script>
export default {
  name: "TabBar",
  methods: {
   scroll: function (message) {
     this.$scrollTo("#" + message, 0, { container: "#slider", cancelable: false, y: false, x: true} );
   }
 }
};
</script>

<style scoped>
p {
  font-family: "Montserrat", sans-serif;
  text-align: center;
  color: #000000;
}

button {
    width: 33.3%;
    font-family: "Montserrat", sans-serif;
    color: #F8F8F8;
    height: 100%;
    border: none;
    border-top: 5px;
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
