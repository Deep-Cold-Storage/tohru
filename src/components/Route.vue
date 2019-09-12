<template>
  <div>
    <section>
      <p><img src="../assets/origin-marker.svg" />From Rzeszów, Tesco</p>
      <p><img src="../assets/destination-marker.svg" />To Kielnarowa, WSiZ</p>
      <button>CHANGE</button>
      <button><img src="../assets/exchange-arrows.svg" /></button>
    </section>
  </div>
</template>

<script>
export default {
  name: "Route",
  props: {
    origin: String,
    destination: String
  }
};
</script>

<style scoped>
p {
  text-align: left;
}

section {
  padding-top: 2vh;
  line-height: 1.5;
  width: 75%;
  margin: 0 auto;
}

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
