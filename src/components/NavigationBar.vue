<template>
  <div class="navigation-bar">
    <div
      class="navigation-bar-button"
      v-bind:class="{ 'nav-button-active': activePage == 'about-page' }"
    >
      <div class="navigation-button-line"></div>
      <button v-on:click="scrollTo('#about-page')">About</button>
    </div>

    <div
      class="navigation-bar-button"
      v-bind:class="{ 'nav-button-active': activePage == 'station-page' }"
    >
      <div class="navigation-button-line"></div>
      <button v-on:click="scrollTo('#station-page')">Station</button>
    </div>

    <div
      class="navigation-bar-button"
      v-bind:class="{ 'nav-button-active': activePage == 'schedule-page' }"
    >
      <div class="navigation-button-line"></div>
      <button v-on:click="scrollTo('#schedule-page')">Schedule</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavigationBar",
  props: {
    activePage: String
  },

  data() {
    return {
      isScrolling: false
    };
  },

  methods: {
    scrollTo: function(target) {
      var self = this;

      if (this.isScrolling == true) {
        return;
      }
      this.isScrolling = true;
      this.$emit("setSnapScroll", false);

      this.$scrollTo(target, 400, {
        container: "#slider",
        easing: "ease",
        cancelable: true,
        y: false,
        x: true,

        onDone: function() {
          self.isScrolling = false;
          self.$emit("setSnapScroll", true);
        },

        onCancel: function() {
          self.isScrolling = false;
          self.$emit("setSnapScroll", true);
        }
      });
    }
  }
};
</script>

<style scoped>
.navigation-bar {
  position: relative;
  height: 50px;
  width: 90vw;

  bottom: 7vh;
  margin: 0 auto;
}

.navigation-button-line {
  transition: background-color 0.4s ease;

  background-color: #353535;
  border-radius: 1000px;
  width: 75%;
  height: 2.5px;
  margin: 0 auto;
}

.navigation-bar-button {
  width: 33.3%;
  height: 100%;
  display: inline-block;
}

.navigation-bar-button button {
  transition: color 0.4s ease;

  width: 100%;
  height: 60%;

  font-family: "Montserrat", sans-serif;
  font-weight: 500;
  font-size: 1.5rem;

  color: #353535;
  background-color: Transparent;

  text-align: center;
  text-decoration: none;

  border: none;
  outline: none;
}

.nav-button-active div {
  background-color: #22a460;
}

.nav-button-active button {
  color: #22a460;
}

@media screen and (min-width: 700px) and (max-width: 1100px) {
  .navigation-bar {
    width: 50vw;
  }
}

@media screen and (min-width: 900px) and (orientation: landscape) {
  .navigation-bar {
    display: none;
  }
}
</style>
