<template>
  <section>
    <p><img class="clock-icon" src="../assets/clock-icon.svg"/>{{selectedDayName}}</p>
    <div class="timetable">
      <transition-group name="timetable-anim">
        <div
          :key="key"
          class="timetable-item"
          v-for="(item, key) in selectedDaySchedule.schedule"
          v-bind:key="key"
        >
          <div class="timetable-item-line"></div>
          <div class="timetable-item-table"><h1 class="text-green">{{ item[0] }}</h1></div>
          <div class="timetable-item-table"><h1 class="text-red">{{ item[1] }}</h1></div>
        </div>
      </transition-group>
    </div>

    <button class="navigation-button" v-on:click="previousDay">PREVIOUS</button>
    <button class="navigation-button navigation-button-boost" v-on:click="nextDay">NEXT</button>
  </section>
</template>

<script>
export default {
  name: "SchedulePageTimetable",
  props: {
    route: Object
  },

  data() {
    return {
      currentDayOffset: 0,
      selectedDayName: "Today",
      selectedDaySchedule: {}
    };
  },

  methods: {
    getScheduleData: function() {
      this.$http
        .get(
          "/v1/schedules/?origin=" +
            this.route.origin +
            "&destination=" +
            this.route.destination +
            "&offset=" +
            this.currentDayOffset
        )
        .then(response => {
          if (response.data.status == "success") {
            this.selectedDaySchedule = response.data.payload;
            this.getDayOfTheWeek()
          } else {
            this.selectedDaySchedule = {};
          }
        })
    },

    getDayOfTheWeek: function() {
      var dataParts = this.selectedDaySchedule.date.split(".")

      var weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

      var date = new Date(dataParts[2], dataParts[1] - 1, dataParts[0]);

      this.selectedDayName = weekdays[date.getDay()] + ", " + this.selectedDaySchedule.date;
    },

    previousDay: function() {
      if (this.currentDayOffset > 0) {
        this.selectedDaySchedule = {};
        this.currentDayOffset = this.currentDayOffset - 1;
      }
    },

    nextDay: function() {
      if (this.currentDayOffset < 30) {
        this.selectedDaySchedule = {};
        this.currentDayOffset = this.currentDayOffset + 1;
      }
    }
  },
  watch: {
    route: {
      deep: true,
      handler: function(route) {
        this.getScheduleData();
      }
    },

    currentDayOffset: function() {
      this.getScheduleData();
    }
  },

  mounted() {
    this.getScheduleData();
  }
};
</script>

<style scoped>
.clock-icon {
  width: 2.0rem;
  height: auto;
  vertical-align: middle;
  margin-right: 10px;
  margin-left: 4px;
}

h1 {
  text-align: center;
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.timetable {
  height: 70vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
}

.timetable-item {
  width: 80%;
  margin: auto;
  scroll-snap-align: start;
}

.timetable-item-table {
  width: 50%;
  display: inline-block;
}


.timetable-item-line {
  background-color: #353535;
  border-radius: 1000px;
  width: 100%;
  height: 2px;
  margin: 0 auto;
}

.navigation-button {
  font-family: "Montserrat", sans-serif;
  height: 4.0rem;
  font-size: 1.5rem;
  font-weight: 700;
  border-radius: 0.8rem;
  margin-top: 20px;
  border: 2px solid #353535;
  background-color: Transparent;

  color: #22a460;
  border: 2px solid #22a460;
  padding-left: 2.0rem;
  padding-right: 2.0rem;

  text-align: center;
  text-decoration: none;
  outline: none;
}

.navigation-button-boost {
    float: right;
    padding-left: 4.0rem;
    padding-right: 4.0rem;
}

.text-green {
  color: #22a460;
}

.text-red {
  color: #fc736a;
}

.timetable-anim-enter-active {
  transition: all 1s ease;
}
.timetable-anim-enter {
  opacity: 0;
}

@media (min-width: 1300px) {
  .timetable::-webkit-scrollbar {
    display: none;
  }
}
</style>
