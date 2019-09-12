<template>
  <div id="app">
    <div id="slider" v-bind:class="{ 'slider-snap': snapScroll }">
      <AboutPage id="about-page"></AboutPage>
      <StationPage id="station-page"></StationPage>
      <SchedulePage id="schedule-page"></SchedulePage>
    </div>
    <TabBar v-on:toggleSnap="toggleSnapScroll"></TabBar>
  </div>
</template>

<script>
import AboutPage from "./components/AboutPage.vue";
import StationPage from "./components/StationPage.vue";
import SchedulePage from "./components/SchedulePage.vue";
import TabBar from "./components/TabBar.vue";

export default {
  name: "app",
  data() {
    return {
      snapScroll: true
    };
  },
  components: {
    AboutPage,
    StationPage,
    SchedulePage,
    TabBar
  },

  methods: {
    toggleSnapScroll: function(boolean) {
      this.snapScroll = boolean;
    }
  },

  mounted() {
    this.$scrollTo("#station-page", 0, {
      container: "#slider",
      cancelable: false,
      force: true,
      y: false,
      x: true
    });
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");

/* CSS Reset */
html {
  box-sizing: border-box;
}

body {
  margin: 0;
  overflow: hidden;
  background-color: #131313;
}

/* Global Text Style */
p {
  font-family: "Montserrat", sans-serif;
  color: #f8f8f8;
  font-size: 15px;
  font-weight: 500;
}

h1 {
  font-family: "Montserrat", sans-serif;
  color: #f8f8f8;
  font-size: 18px;
}

h2 {
  font-family: "Montserrat", sans-serif;
  color: #f8f8f8;
  font-size: 23px;
}

/* Slider, Pages */
#slider {
  overflow-x: scroll;
  display: flex;
}

.slider-snap {
  scroll-snap-type: x mandatory;
}

#about-page,
#station-page,
#schedule-page {
  border: 0;
  height: 100vh;
  min-width: 100vw;
  scroll-snap-stop: always;
  scroll-snap-align: center;
}

@media screen and (min-width: 900px) and (orientation: landscape) {
  #about-page,
  #station-page,
  #schedule-page {
    min-width: 33.33vw;
  }
}
</style>
