<template>
  <section>
    <p><img class="icon" alt="gears" src="../assets/cogs-icon.svg" />Options</p>
    <p>
      Use Smart-Route :
      <button
        class="toggle-button"
        v-bind:class="{ 'toggle-button-green': useSmartRoute }"
        v-on:click="setSmartRoute(true)"
      >
        YES
      </button>
      <button
        class="toggle-button"
        v-bind:class="{ 'toggle-button-red': !useSmartRoute }"
        v-on:click="setSmartRoute(false)"
      >
        NO
      </button>
    </p>
    <p class="text-gray">
      Predicts route based on usage history and location data.
    </p>
  </section>
</template>

<script>
export default {
  name: "AboutPageOptions",
  props: {
    useSmartRoute: Boolean
  },

  methods: {
    // Sets global Smart-Route setting
    setSmartRoute: function(boolean) {
      this.$emit("setSmartRoute", boolean);
    }
  }
};
</script>

<style scoped>
button {

  font-family: "Montserrat", sans-serif;
  font-size: 1.5rem;
  font-weight: 700;
  height: 4rem;

  background-color: Transparent;

  border-radius: 0.8rem;

  padding-left: 1rem;
  padding-right: 1rem;
  margin-left: 0.5rem;
  margin-right: 0.5rem;

  text-align: center;
  text-decoration: none;
  outline: none;
}

.icon {
  width: 2rem;
  height: auto;
  vertical-align: middle;
  margin-right: 10px;
  margin-left: 4px;
}

.toggle-button {
  transition: all 0.2s ease;
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

.text-gray {
  color: #353535;
}
</style>
