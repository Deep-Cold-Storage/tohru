<template>
  <div id="app">
    <SelectPage
      v-show="showSelectPage"
      class="page-overlay"
      v-bind:route="route"
      v-on:toggleSelectPage="toggleSelectPage"
      v-on:setRoute="setRoute"
    />

    <div
      id="slider"
      v-show="!showSelectPage"
      v-bind:class="{ 'slider-snap-active': snapSliderScroll }"
    >
      <AboutPage
        id="about-page"
        class="page"
        v-on:setSmartRoute="setSmartRoute"
        v-bind:useSmartRoute="useSmartRoute"
        v-observe-visibility="{
          callback: visibilityChange,
          throttle: 0,
          intersection: { threshold: 1, rootMargin: '20%' }
        }"
      />

      <StationPage
        id="station-page"
        class="page"
        v-on:toggleSelectPage="toggleSelectPage"
        v-on:setRoute="setRoute"
        v-bind:route="route"
        v-observe-visibility="{
          callback: visibilityChange,
          throttle: 0,
          intersection: { threshold: 1, rootMargin: '20%' }
        }"
      />

      <SchedulePage
        id="schedule-page"
        class="page"
        v-bind:route="route"
        v-observe-visibility="{
          callback: visibilityChange,
          throttle: 0,
          intersection: { threshold: 1, rootMargin: '20%' }
        }"
      />
    </div>

    <NavigationBar
      v-show="!showSelectPage"
      v-on:setSnapScroll="setSnapScroll"
      v-bind:activePage="activePage"
    />

  </div>
</template>

<script>
import AboutPage from "./components/AboutPage.vue";
import SelectPage from "./components/SelectPage.vue";
import StationPage from "./components/StationPage.vue";
import SchedulePage from "./components/SchedulePage.vue";
import NavigationBar from "./components/NavigationBar.vue";

export default {
  name: "app",
  data() {
    return {
      // Used by navigation bar
      activePage: "station-page",

      route: {
        origin: "tesc",
        destination: "ctir"
      },

      // UI State
      showSelectPage: false,
      snapSliderScroll: true,

      // Used by Smart Route system
      useSmartRoute: false,
      lastUsedDestinations: []
    };
  },

  components: {
    AboutPage,
    SelectPage,
    StationPage,
    SchedulePage,
    NavigationBar
  },

  methods: {
    // Used to change UI state
    toggleSelectPage: function() {
      this.showSelectPage = !this.showSelectPage;
    },

    setSnapScroll: function(bool) {
      this.snapSliderScroll = bool;
    },

    // Used by navigation bar
    visibilityChange: function(isVisible, object) {
      if (isVisible === true) {
        this.activePage = object.target.id;
      }
    },

    // Sets new global selected route
    setRoute: function(route) {
      this.route = route;

      // Saves selected destinations for Smart-Route
      this.lastUsedDestinations.push(route.destination);

      if (this.lastUsedDestinations.length > 6) {
        this.lastUsedDestinations.shift();
      }
    },

    // Smart-Route system
    setSmartRoute: function(bool) {
      this.useSmartRoute = bool;
    },

    selectSmartRoute: function() {
      navigator.geolocation.getCurrentPosition(success);
      var self = this;

      function success(pos) {
        var crd = pos.coords;

        self.$http
          .get(
            "/v1/origins/geo/?lat=" +
              crd.longitude +
              "&lng=" +
              crd.latitude +
              "&active=true"
          )
          .then(response => {
            if (response.data.status == "success") {
              var reversedDestinations = self.lastUsedDestinations.reverse();
              var nearestOrigin = Object.keys(response.data.payload)[0];
              var originConnections = response.data.payload[nearestOrigin].connections;

              for (var i = 0; i < reversedDestinations.length; ++i) {
                if (originConnections.includes(reversedDestinations[i])) {
                  self.setRoute({
                    origin: nearestOrigin,
                    destination: reversedDestinations[i]
                  });
                  return null;
                }
              }
            }
          });
      }
    }
  },

  mounted() {
    // Scrolls to Station Page on load
    this.$scrollTo("#station-page", 0, {
      container: "#slider",
      cancelable: false,
      force: true,
      y: false,
      x: true
    });

    // Loads saved settings from Local Storage
    if (localStorage.route) {
      this.route = JSON.parse(localStorage.route);
    }

    if (localStorage.useSmartRoute) {
      this.useSmartRoute = JSON.parse(localStorage.useSmartRoute);
    }

    if (localStorage.lastUsedDestinations) {
      this.lastUsedDestinations = JSON.parse(localStorage.lastUsedDestinations);
    }

    this.selectSmartRoute();
  },

  watch: {
    // Saves route between app uses
    route: {
      deep: true,
      handler: function(route) {
        localStorage.route = JSON.stringify(route);
      }
    },

    // Smart-Route
    useSmartRoute(bool) {
      localStorage.useSmartRoute = bool;
    },

    lastUsedDestinations(array) {
      localStorage.lastUsedDestinations = JSON.stringify(array);
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=block");

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

/* Global Misc */
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

.page {
  border: 0;
  height: 100vh;
  min-width: 100vw;
  scroll-snap-stop: always;
  scroll-snap-align: center;
}

/* Modal */
.page-overlay {
  border: 0;
  height: 100vh;
  width: 100vw;
}

/* Animations */
@keyframes reveal {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 100;
  }
}

/* Small Phones (Portrait) */
@media screen and (max-width: 359px) {
  html {
    font-size: 7px;
  }
}

/* All Phones (Landscape) */
@media (max-width: 1000px) and (min-aspect-ratio: 13/9) {
  body {
    opacity: 0;
  }
}

/* Tablets (Portrait) */
@media screen and (min-width: 750px) and (max-width: 1300px) {
  section {
    width: 40%;
  }

  body {
    background-size: 100%;
  }
}

/* Desktop (Landscape) */
@media (min-width: 1300px) {
  html {
    font-size: 11px;
  }

  body {
    background-size: 50%;
    background-position: 40% 50%;
  }

  section {
    width: 70%;
  }

  .page {
    min-width: 33.33vw;
  }

  .page-overlay {
    width: 33.3vw;
    margin: 0 auto;
  }
}
</style>
