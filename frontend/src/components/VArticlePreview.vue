<template>
  <div class="article-preview">
    <RwvArticleMeta isPreview :favorite="favorite" />
    <router-link :to="articleLink" class="preview-link">
      <h1 v-text="favorite.title" />
      <p v-text="favorite.description" />
      <span>Read more...</span>
    </router-link>
  </div>
</template>

<script>

export default {
  name: "RwvArticlePreview",
  components: {
  },
  props: {
    favorite: { type: Object, required: true }
  },
  computed: {
    articleLink() {
      return {
        name: "favorite",
      };
    }
  }
};
</script>
