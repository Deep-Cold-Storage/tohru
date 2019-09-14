<template>
  <div>
    <SchedulePageTimetable v-bind:route="route"/>
  </div>
</template>

<script>
import SchedulePageTimetable from "./SchedulePageTimetable.vue";

export default {
  name: "SchedulePage",
  components: {
    SchedulePageTimetable,
  },
  props: {
    route: Object,
  }
};
</script>

<style scoped>
</style>
