<template>
  <div>
    <div v-if="isLoading" class="article-preview">Loading articles...</div>
    <div v-else>
      <div v-if="favorites.length === 0" class="article-preview">
        No favorites are here... yet.
      </div>
      <RwvArticlePreview
        v-for="(favorite, index) in favorites"
        :favorite="favorite"
        :key="favorite.favorite + index"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import RwvArticlePreview from "./VArticlePreview";
import {FETCH_FAVORITES} from "../store/actions.type";

export default {
  name: "RwvArticleList",
  components: {
    RwvArticlePreview
  },
  data() {
    return {
      currentPage: 1
    };
  },
  computed: {
    listConfig() {
      const { type } = this;
      const filters = {
        offset: (this.currentPage - 1) * this.itemsPerPage,
        limit: this.itemsPerPage
      };
      if (this.author) {
        filters.author = this.author;
      }
      if (this.tag) {
        filters.tag = this.tag;
      }
      if (this.favorited) {
        filters.favorited = this.favorited;
      }
      return {
        type,
        filters
      };
    },

    ...mapGetters([ "isLoading", "favorites"])
  },
  mounted() {
    this.fetchArticles();
  },
  methods: {
    fetchArticles() {
      this.$store.dispatch(FETCH_FAVORITES, this.listConfig);
    }
  }
};
</script>
