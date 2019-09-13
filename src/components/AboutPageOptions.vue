<template>
  <section>
    <p><img class="icon" src="../assets/cogs-icon.svg" />Options</p>
    <p>
      Use GPS :
      <button
        v-bind:class="{ 'toggle-button-green': useGPS }"
        class="toggle-button"
      >
        YES
      </button>
      <button
        v-bind:class="{ 'toggle-button-red': !useGPS }"
        class="toggle-button"
      >
        NO
      </button>
    </p>
  </section>
</template>

<script>
export default {
  name: "AboutPageOptions",
  props: {
    useGPS: Boolean
  }
};
</script>

<style scoped>
.icon {
  width: 20px;
  height: auto;
  vertical-align: middle;
  margin-right: 10px;
  margin-left: 4px;
}

button {
  height: 40px;

  font-family: "Montserrat", sans-serif;
  font-size: 15px;
  font-weight: 700;

  text-align: center;
  text-decoration: none;

  color: #22a460;
  background-color: Transparent;

  padding-left: 10px;
  padding-right: 10px;

  margin-left: 10px;
  margin-right: 10px;

  border-radius: 8px;
  border: 2px solid #22a460;

  outline: none;
}

.toggle-button {
  border: 2px solid #353535;
  color: #353535;
}

.toggle-button-red {
  border: 2px solid #fc736a;
  color: #fc736a;
}

.toggle-button-green {
  border: 2px solid #22a460;
  color: #22a460;
}
</style>
