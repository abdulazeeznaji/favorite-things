<template>
  <footer>
    <div class="container">
      <router-link class="logo-font" :to="{ name: 'home', params: {} }">
        Insurance - Magic
      </router-link>
      <span class="attribution">
        Your favorite place for your favorite things
        <a rel="noopener noreferrer" target="blank"
          ></a>
      </span>
    </div>
  </footer>
</template>

<script>
export default {
  name: "RwvFooter"
};
</script>