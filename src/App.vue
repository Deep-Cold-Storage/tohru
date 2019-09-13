<template>
  <div id="app">
    <div v-show="isSelectingRoute" class="modal-page">
      <SelectPage
        v-bind:route="route"
        v-on:toggleSelectionPage="toggleSelectionPage"
        v-on:setRoute="setRoute"
      />
    </div>

    <div
      id="slider"
      v-show="!isSelectingRoute"
      v-bind:class="{ 'slider-snap-active': snapScroll }"
    >
      <AboutPage
        id="about-page"
        v-bind:useGPS="useGPS"
        v-observe-visibility="{
          callback: visibilityChanged,
          throttle: 0,
          intersection: { threshold: 1, rootMargin: '20%' }
        }"
      />
      <StationPage
        id="station-page"
        v-on:toggleSelectionPage="toggleSelectionPage"
        v-on:setRoute="setRoute"
        v-bind:route="route"
        v-observe-visibility="{
          callback: visibilityChanged,
          throttle: 0,
          intersection: { threshold: 1, rootMargin: '20%' }
        }"
      />
      <SchedulePage
        id="schedule-page"
        v-bind:route="route"
        v-observe-visibility="{
          callback: visibilityChanged,
          throttle: 0,
          intersection: { threshold: 1, rootMargin: '20%' }
        }"
      />
    </div>
    <NavigationBar
      v-show="!isSelectingRoute"
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
import SelectPage from "./components/SelectPage.vue";
export default {
  name: "app",
  data() {
    return {
      snapScroll: true,
      visiblePage: "station-page",

      useGPS: false,
      isSelectingRoute: false,

      route: {
        origin: "tesc",
        destination: "ctir"
      }
    };
  },

  components: {
    AboutPage,
    StationPage,
    SchedulePage,
    SelectPage,
    NavigationBar
  },

  methods: {
    toggleSnapScroll: function(boolean) {
      this.snapScroll = boolean;
    },

    toggleSelectionPage: function() {
      this.isSelectingRoute = !this.isSelectingRoute;
    },

    setRoute: function(new_route) {
      this.route = new_route;
    },

    visibilityChanged(isVisible, entry) {
      if (isVisible == true) {
        this.visiblePage = entry.target.id;
      }
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

  background-image: url("./assets/tohru-bg.svg");
  background-repeat: no-repeat;
  background-position: 90% 50%;
  background-size: 160%;
}

/* Global Text Style */
p {
  font-family: "Montserrat", sans-serif;
  color: #f8f8f8;
  font-size: 1.5rem;
  font-weight: 500;
  text-align: left;
  letter-spacing: 0.04em;
}

h1 {
  font-family: "Montserrat", sans-serif;
  color: #f8f8f8;
  font-size: 1.8rem;
  font-weight: 500;
  text-align: left;
  letter-spacing: 0.08em;
}

h2 {
  font-family: "Montserrat", sans-serif;
  color: #f8f8f8;
  font-size: 2.3rem;
  font-weight: 600;
  text-align: left;
  letter-spacing: 0.04em;
}
/* Global Section */
section {
  width: 78%;
  margin: 0 auto;
  padding-top: 2vh;
  line-height: 1.5;
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

/* Modal */
.modal-page {
  border: 0;
  height: 100vh;
  width: 100vw;
}

@media screen and (min-width: 100px) and (max-width: 340px) {
  html {
    font-size: 9px;
  }
}

@media screen and (min-width: 700px) and (max-width: 1100px) {
  section {
    width: 40%;
  }
  body {
    background-size: 100%;
  }
}

@media screen and (min-width: 900px) and (orientation: landscape) {
  #about-page,
  #station-page,
  #schedule-page {
    min-width: 33.33vw;
  }
  section {
    width: 70%;
  }
  .modal-page {
    width: 33.3vw;
    margin: 0 auto;
  }
  html {
    font-size: 11px;
  }
  body {
    background-size: 50%;
    background-position: 40% 50%;
  }
}
</style>
