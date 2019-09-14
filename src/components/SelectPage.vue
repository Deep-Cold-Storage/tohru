<template>
  <section>
    <h2>Route selection</h2>
    <template v-if="!isOriginSelected">
      <p>
        <img class="location-icon" src="../assets/origin-marker.svg" />Select
        <span class="green">Origin</span>
      </p>
      <div v-for="(item, key) in allOrigins" v-bind:key="item.name">
        <button
          class="select-button"
          v-on:click="selectOrigin(key)"
          v-bind:class="{ 'selected-green': checkOriginSelection(key) }"
        >
          {{ item.name }}
        </button>
      </div>
      <button class="navigation-button selected-red" v-on:click="cancelSelection()">CANCEL</button>
      <button class="navigation-button selected-green witdh-boost" v-on:click="nextSelection()">NEXT</button>
    </template>

    <template v-if="isOriginSelected">
      <p>
        <img
          class="location-icon"
          src="../assets/destination-marker.svg"
        />Select <span class="red">Destination</span>
      </p>
      <div v-for="(item, key) in allDestinations" v-bind:key="item.name">
        <button
          class="select-button"
          v-on:click="selectDestination(key)"
          v-bind:class="{ 'selected-red': checkDestinationSelection(key) }"
        >
          {{ item.name }}
        </button>
      </div>
      <button class="navigation-button selected-red"  v-on:click="cancelSelection()">CANCEL</button>
      <button class="navigation-button selected-green witdh-boost" v-on:click="acceptSelection()">ACCEPT</button>
    </template>
  </section>
</template>

<script>
export default {
  name: "SelectPage",
  data() {
    return {
      isOriginSelected: false,

      allOrigins: Object,

      selectedOrigin: this.route.origin,
      selectedDestination: this.route.destination
    };
  },
  props: {
    route: Object
  },
  methods: {
    getAllOrigins: function() {
      this.$http
        .get("https://tohru.sylvanas.dream/origins/")
        .then(response => {
          if (response.data.status == "success") {
            this.allOrigins = response.data.payload;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    checkOriginSelection: function(origin_code) {
      if (this.selectedOrigin === origin_code) {
        return true;
      }
      return false;
    },
    checkDestinationSelection: function(destination_code) {
      if (this.selectedDestination === destination_code) {
        return true;
      }
      return false;
    },

    selectOrigin: function(origin_code) {
      this.selectedOrigin = origin_code;
    },
    selectDestination: function(destination_code) {
      this.selectedDestination = destination_code;
    },
    acceptSelection: function() {
      this.$emit("setRoute", {
        origin: this.selectedOrigin,
        destination: this.selectedDestination
      });
      this.$emit("toggleSelectionPage");
      this.isOriginSelected = false;
    },
    cancelSelection: function() {
      this.$emit("toggleSelectionPage");
      this.isOriginSelected = false;
      this.selectedOrigin = this.route.origin;
      this.selectedDestination = this.route.destination;
    },
    nextSelection: function() {
      this.isOriginSelected = true;
    }
  },
  computed: {
    allDestinations: function() {
      var connections = this.allOrigins[this.selectedOrigin].connections;
      var allDestinations = {};

      for (var i = 0; i < connections.length; i++) {
        if (connections[i] in this.allOrigins) {
          allDestinations[connections[i]] = this.allOrigins[connections[i]];
        }
      }
      return allDestinations;
    }
  },
  created() {
    this.getAllOrigins();
  }
};
</script>

<style scoped>
.location-icon {
  width: 14px;
  height: auto;
  vertical-align: middle;
  margin-right: 8px;
  margin-left: 4px;
}

.select-button {
  transition: all 0.3s ease;

  font-family: "Montserrat", sans-serif;
  color: #f8f8f8;
  height: 40px;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 700;
  width: 100%;
  margin-top: 8px;
  border: 2px solid #353535;
  display: block;
  background-color: Transparent;
  outline: none;
}

.witdh-boost {
  padding-left: 50px;
  padding-right: 50px;
  float: right;
}

.navigation-button {
  font-family: "Montserrat", sans-serif;
  height: 40px;
  font-size: 15px;
  font-weight: 700;
  border-radius: 8px;
  margin-top: 50px;
  border: 2px solid #353535;
  background-color: Transparent;
}

.green {
  color: #22a460;
}
.selected-green {
  color: #22a460;
  border: 2px solid #22a460;
}

.selected-red {
  color: #fc736a;
  border: 2px solid #fc736a;
}
.red {
  color: #fc736a;
}
</style>
