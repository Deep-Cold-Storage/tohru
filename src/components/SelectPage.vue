<template>
  <section>
    <h2>Route selection</h2>
    <template v-if="!isOriginSelected">
      <p>Select origin</p>
      <div v-for="(item, key) in allOrigins" v-bind:key="item.name">
        <button class="select-button"
          v-on:click="selectOrigin(key)"
          v-bind:class="{ 'selected-green': checkOriginSelection(key) }"
        >
          {{ item.name }}
        </button>
      </div>
    </template>

    <template v-if="isOriginSelected">
      <p>Select destination</p>
      <div v-for="(item, key) in allDestinations" v-bind:key="item.name">
        <button class="select-button"
          v-on:click="selectDestination(key)"
          v-bind:class="{ 'selected-red': checkDestinationSelection(key) }"
        >
          {{ item.name }}
        </button>
      </div>
      <button v-on:click="acceptSelection()">ACCEPT</button>
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
      selectedDestination: this.route.destination,
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
      };
      return false;
    },
    checkDestinationSelection: function(destination_code) {
      if (this.selectedDestination === destination_code) {
        return true;
      };
      return false;
    },

    selectOrigin: function(origin_code) {
      this.isOriginSelected = true;
      this.selectedOrigin = origin_code;
    },
    selectDestination: function(destination_code) {
      this.selectedDestination = destination_code;
    },
    acceptSelection: function() {
      this.$emit("setRoute", {"origin": this.selectedOrigin, "destination": this.selectedDestination});
      this.$emit("toggleSelectionPage");
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

.select-button {
  font-family: "Montserrat", sans-serif;
  color: #f8f8f8;
  height: 40px;
  width: 100%;
  margin-top: 8px;
  border: 2px solid #353535;
}

button {
  font-family: "Montserrat", sans-serif;
  font-size: 15px;
  font-weight: 700;
  padding: 10px;
  width: 40%;
  text-align: center;
  text-decoration: none;

  color: #22A460;
  background-color: Transparent;

  padding-left: 10px;
  padding-right: 10px;

  border-radius: 8px;
  border: 2px solid #22A460;

  outline: none;
  display: block;
  margin-top: 10vh;
  margin-bottom: 1vh;
  margin-left: auto;
  margin-right: auto;
}

.selected-green {
  color: #22a460;
  border: 2px solid #22a460;
}

.selected-red {
  color: #FC736A;
  border: 2px solid #FC736A;
}
</style>
