<template>
  <div id="app">
    <div id="slider" v-bind:class="{ 'slider-snap-active': snapScroll }">
      <AboutPage
        id="about-page"
        v-observe-visibility="{
          callback: visibilityChanged,
          throttle: 0,
          intersection: { threshold: 1, rootMargin: '20%' }
        }"/>
      <StationPage
        id="station-page"
        v-observe-visibility="{
          callback: visibilityChanged,
          throttle: 0,
          intersection: { threshold: 1, rootMargin: '20%' }
        }"/>
      <SchedulePage
        id="schedule-page"
        v-observe-visibility="{
          callback: visibilityChanged,
          throttle: 0,
          intersection: { threshold: 1, rootMargin: '20%' }
        }"/>
    </div>
    <NavigationBar
      v-on:toggleSnap="toggleSnapScroll"
      v-bind:visiblePage="visiblePage"
    />
  </div>
</template>

<script>
import AboutPage from "./components/AboutPage.vue";
import StationPage from "./components/StationPage.vue";
import SchedulePage from "./components/SchedulePage.vue";
import NavigationBar from "./components/NavigationBar.vue";

export default {
  name: "app",
  data() {
    return {
      snapScroll: true,
      visiblePage: "station-page"
    };
  },

  components: {
    AboutPage,
    StationPage,
    SchedulePage,
    NavigationBar
  },

  methods: {
    toggleSnapScroll: function(boolean) {
      this.snapScroll = boolean;
    },

    visibilityChanged(isVisible, entry) {
      if (isVisible == true) {
        this.visiblePage = entry.target.id;
      };
    }
  },

  mounted() {
    this.$scrollTo("#station-page", 0, {
      container: "#slider",
      cancelable: false,
      force: true,
      y: false,
      x: true
      }
    );
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");

/* CSS Reset */
html {
  box-sizing: border-box;
  font-size: 10px;
}

*,
*:before,
*:after {
  box-sizing: inherit;
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
  font-size: 1.5rem;
  font-weight: 500;
  letter-spacing: 0.04em;
}

h1 {
  font-family: "Montserrat", sans-serif;
  color: #f8f8f8;
  font-size: 1.8rem;
  letter-spacing: 0.08em;
}

h2 {
  font-family: "Montserrat", sans-serif;
  color: #f8f8f8;
  font-size: 2.3rem;
  letter-spacing: 0.04em;
}

/* Slider, Pages */
#slider {
  overflow-x: scroll;
  display: flex;
}

.slider-snap-active {
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
