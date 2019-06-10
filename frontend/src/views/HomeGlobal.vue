<template>
  <div class="home-global"><RwvArticleList type="all" /></div>
</template>
<script>
import RwvArticleList from "@/components/FavoritesList.vue";

export default {
  name: "rwv-home-global",
  components: {
    RwvArticleList
  }
};
</script>
