<template>
  <section>
    <template v-if="!noDeparturesError">
      <h2>Departure in <span class="text-green">{{ liveStationData.until }}</span> min</h2>
      <h2>At <span class="text-green">{{ liveStationData.schedule[0][0] }}</span></h2>
      <h2>Arriving at <span class="text-red">{{ liveStationData.schedule[0][1] }}</span></h2>
    </template>

    <template v-if="noDeparturesError">
      <h2 class="text-red">No departures !</h2>
      <p>Tohru couldn't find any close departures for today!</p>
      <p>You could always try to change selected route.</p>
    </template>
  </section>
</template>

<script>
export default {
  name: "StationPageLive",
  props: {
    route: Object
  },

  data() {
    return {
      noDeparturesError: false,
      intervalTimer: Object,
      liveStationData: { until: "00", schedule: [["00:00", "00:00"]] }
    };
  },

  methods: {
    // Gets info about nearest departure from selected origin
    getStationLiveData: function() {
      this.$http
        .get(
          "/v1/live/?origin=" +
            this.route.origin +
            "&destination=" +
            this.route.destination
        )
        .then(response => {
          if (response.data.status == "success") {
            this.liveStationData = response.data.payload;
            this.noDeparturesError = false;
          } else {
            this.liveStationData = { until: "00", schedule: [["00:00", "00:00"]] };
            this.noDeparturesError = true;
          }
        })
    }
  },
  watch: {
    route: {
      deep: true,
      handler: function(route) {
        this.getStationLiveData();
      }
    }
  },
  created() {
    this.getStationLiveData();

    var self = this;
    this.intervalTimer = setInterval(function() {
      self.getStationLiveData();
    }, 3600);
  }
};
</script>

<style scoped>
span {
  font-size: 3rem;
}

section {
  padding-top: 10vh;
}

.text-green {
  color: #22a460;
}

.text-red {
  color: #fc736a;
}
</style>
