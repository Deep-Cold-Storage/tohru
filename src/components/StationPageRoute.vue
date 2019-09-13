<template>
  <section>
    <p><img src="../assets/origin-marker.svg" />From {{ originName }}</p>
    <p>
      <img src="../assets/destination-marker.svg" />To {{ destinationName }}
    </p>
    <button v-on:click="toggleSelectionPage()">CHANGE</button>
    <button v-on:click="flipRoute()"><img src="../assets/exchange-arrows.svg" /></button>
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
    getOrignName: function() {
      this.$http
        .get("https://tohru.sylvanas.dream/origins/" + this.route.origin)
        .then(response => {
          if (response.data.status == "success") {
            this.originName = response.data.payload[this.route.origin].name;
          } else {
            this.originName = "Hello";
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    getDestinationName: function() {
      this.$http
        .get("https://tohru.sylvanas.dream/origins/" + this.route.destination)
        .then(response => {
          if (response.data.status == "success") {
            this.destinationName =
              response.data.payload[this.route.destination].name;
          } else {
            this.destinationName = "Hello";
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    flipRoute: function() {
      this.$emit("setRoute", {"origin": this.route.destination, "destination": this.route.origin});
    },

    toggleSelectionPage: function() {
      this.$emit("toggleSelectionPage");
    }
  },
  created() {
    this.getOrignName();
    this.getDestinationName();
  },
  watch: {
    "route.origin": function() {
      this.getOrignName();
    },
    "route.destination": function() {
      this.getDestinationName();
    }
  }
};
</script>

<style scoped>
img {
  width: 14px;
  height: auto;
  vertical-align: middle;
  margin-right: 4px;
  margin-left: 4px;
}

button {
  font-family: "Montserrat", sans-serif;
  color: #353535;
  height: 40px;
  padding-left: 10px;
  padding-right: 10px;
  margin-right: 10px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 15px;
  text-align: center;
  text-decoration: none;
  border: 2px solid #353535;
  outline: none;
  background-color: Transparent;
}
</style>
