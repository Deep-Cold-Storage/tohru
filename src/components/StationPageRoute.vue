<template>
  <section>
    <p><img class="location-icon" src="../assets/origin-marker.svg" />From {{ originName }}</p>
    <p><img class="location-icon" src="../assets/destination-marker.svg" />To {{ destinationName }}</p>
    <button v-on:click="toggleSelectPage">CHANGE</button>
    <button v-on:click="flipRoute">
      <img class="flip-icon" src="../assets/exchange-arrows.svg" />
    </button>
  </section>
</template>

<script>
export default {
  name: "StationPageRoute",
  props: {
    route: Object
  },
  data() {
    return {
      originName: "",
      destinationName: ""
    };
  },
  methods: {
    // Gets name of origin from code
    getOriginName: function() {
      this.$http
        .get("/v1/origins/" + this.route.origin)
        .then(response => {
          if (response.data.status == "success") {
            this.originName = response.data.payload[this.route.origin].name;
          }
        })
    },

    // Gets name of destination from code
    getDestinationName: function() {
      this.$http
        .get("/v1/origins/" + this.route.destination)
        .then(response => {
          if (response.data.status == "success") {
            this.destinationName =
              response.data.payload[this.route.destination].name;
          } else {
            this.destinationName = "Hello";
          }
        })
    },

    // Flips origin, destination globally
    flipRoute: function() {

      // Temp swicht for faster feedback
      var temp = this.originName;
      this.originName = this.destinationName;
      this.destinationName = temp;

      this.$emit("setRoute", {
        origin: this.route.destination,
        destination: this.route.origin
      });
    },

    toggleSelectPage: function() {
      this.$emit("toggleSelectPage");
    }
  },
  
  created() {
    this.getOriginName();
    this.getDestinationName();
  },

  watch: {
    "route.origin": function() {
      this.getOriginName();
    },
    "route.destination": function() {
      this.getDestinationName();
    }
  }
};
</script>

<style scoped>
.location-icon {
  width: 1.4rem;
  height: auto;
  vertical-align: middle;
  margin-right: 8px;
  margin-left: 4px;
}

.flip-icon {
  width: 1.4rem;
  height: auto;
  vertical-align: middle;
  margin-right: 4px;
  margin-left: 4px;
}

button {
  font-family: "Montserrat", sans-serif;
  color: #353535;
  height: 4rem;
  padding-left: 1rem;
  padding-right: 1rem;
  margin-right: 1rem;
  border-radius: 8px;
  font-weight: 700;
  font-size: 1.5rem;
  text-align: center;
  text-decoration: none;
  border: 2px solid #353535;
  outline: none;
  background-color: Transparent;
}
</style>
