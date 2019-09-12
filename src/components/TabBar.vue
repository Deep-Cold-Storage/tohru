<template>
  <nav class="tab-bar">
    <div
      class="nav-button"
      v-bind:class="{ 'nav-button-active': visiblePage == 'about-page' }"
    >
      <div class="nav-button-line"></div>
      <button v-on:click.stop="scroll('#about-page')">About</button>
    </div>

    <div
      class="nav-button"
      v-bind:class="{ 'nav-button-active': visiblePage == 'station-page' }"
    >
      <div class="nav-button-line"></div>
      <button v-on:click.stop="scroll('#station-page')">Station</button>
    </div>

    <div
      class="nav-button"
      v-bind:class="{ 'nav-button-active': visiblePage == 'schedule-page' }"
    >
      <div class="nav-button-line"></div>
      <button v-on:click.stop="scroll('#schedule-page')">Schedule</button>
    </div>
  </nav>
</template>

<script>
export default {
  name: "TabBar",
  props: {
    visiblePage: String
  },
  data() {
    return {
      isScrolling: false
    };
  },
  methods: {
    scroll: function(target) {
      var self = this;

      if (this.isScrolling == true) {
        return;
      }
      this.isScrolling = true;
      this.$emit("toggleSnap", false);

      this.$scrollTo(target, 400, {
        container: "#slider",
        easing: "ease",
        cancelable: true,
        y: false,
        x: true,

        onDone: function() {
          self.isScrolling = false;
          self.$emit("toggleSnap", true);
        },

        onCancel: function() {
          self.isScrolling = false;
          self.$emit("toggleSnap", true);
        }
      });
    }
  }
};
</script>

<style scoped>
/* Active Button */
.nav-button-active div {
  background-color: #22a460;
}

.nav-button-active button {
  color: #22a460;
}

button {
  transition: color 0.4s ease;

  width: 100%;
  height: 60%;

  font-family: "Montserrat", sans-serif;
  color: #353535;
  font-weight: 500;
  font-size: 15px;
  text-align: center;
  text-decoration: none;

  border: none;
  outline: none;
  background-color: Transparent;
}

.nav-button {
  width: 33.3%;
  height: 100%;
  display: inline-block;
}

.nav-button-line {
  transition: background-color 0.4s ease;
  background-color: #353535;
  border-radius: 1000px;
  width: 75%;
  height: 5%;
  margin: 0 auto;
}

.tab-bar {
  position: relative;
  height: 50px;
  width: 90vw;
  bottom: 7vh;
  margin: 0 auto;
}

@media screen and (min-width: 700px) and (max-width: 1100px) {
  .tab-bar {
    width: 50vw;
  }
}

@media screen and (min-width: 900px) and (orientation: landscape) {
  .tab-bar {
    display: none;
  }
}
</style>
