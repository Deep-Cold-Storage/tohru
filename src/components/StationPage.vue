<template>
  <div class="station-page">
    <Route></Route>
    <StationLive v-bind:payload="payload"></StationLive>
  </div>
</template>

<script>
import Route from "./Route.vue";
import StationLive from "./StationLive.vue";

export default {
  name: "StationPage",
  components: {
    Route,
    StationLive
  },
  props: {
    origin: String,
    destination: String
  },
  data() {
    return {
      payload: {}
    }
  },
  methods: {
    getLiveData: function() {
      this.$http
        .get('https://tohru.sylvanas.dream/live/?origin=tesc&destination=ctir')
        .then(response => {
          console.log("Run!")
          if (response.data.status == "success"){
            this.payload = response.data.payload;
          } else {
            this.payload = {};
          }
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted() {
    var self = this
    const interval = setInterval(function() {self.getLiveData()}, 1000);
  }
};
</script>

<style scoped>
p {
  text-align: center;
}
</style>
