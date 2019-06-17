<template>
  <div class="editor-page">
    <div class="container page">
      <div class="row">
        <div class="col-md-10 offset-md-1 col-xs-12">
          <RwvListErrors :errors="errors" />
          <form v-on:submit.prevent="onPublish(favorite.slug);">
            <fieldset :disabled="inProgress">
              <fieldset class="form-group">
                <input
                        type="text"
                        class="form-control form-control-lg"
                        v-model="favorite.title"
                        placeholder="Title"
                />
              </fieldset>
              <fieldset class="form-group">
                <input
                        type="text"
                        class="form-control"
                        v-model="favorite.description"
                        placeholder="Description"
                />
              </fieldset>
              <fieldset class="form-group">
                <input
                        type="number"
                        class="form-control"
                        v-model="favorite.ranking"
                        placeholder="Ranking"
                />
              </fieldset>
              <fieldset class="form-group">
                <select v-model="favorite.selected">
                  <option v-for="category in favorite.categories" v-bind:value="category.id">
                    {{ category.name }}
                  </option>
                </select>
              </fieldset>
              <fieldset class="form-group">
                <input
                        disabled
                        class="form-control"
                        v-model="favorite.created_date"
                        placeholder="Ranking"
                />
              </fieldset>
              <fieldset class="form-group">
              </fieldset>
            </fieldset>
            <button
                    :disabled="inProgress"
                    class="btn btn-lg pull-xs-right btn-primary"
                    type="submit"
            >
              Publish Favorite
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters } from "vuex";
  import store from "@/store";
  import RwvListErrors from "@/components/ListErrors";
  import {
    FAVORITE_PUBLISH,
    FETCH_CATEGORIES
  } from "@/store/actions.type";

  export default {
    name: "RwvFavoriteEdit",
    components: { RwvListErrors },
    props: {
      previousFavorite: {
        type: Object,
        required: false
      }
    },
    data() {
      return {
        tagInput: null,
        inProgress: false,
        errors: {}
      };
    },
    beforeRouteEnter(to, from, next) {
      Promise.all([
        store.dispatch(FETCH_CATEGORIES, to.params.slug),
      ]).then(() => {
      next();
      });
    },
    computed: {
      ...mapGetters(["favorite", "categories", "selected"])
    },
    methods: {
      onPublish(slug) {
        let action = FAVORITE_PUBLISH;
        this.inProgress = true;
        this.$store
                .dispatch(action)
                .then(({ data }) => {
                  this.inProgress = false;
                  this.$router.push({
                    name: "home",
                    params: { slug: data.favorite.id }
                  });
                })
                .catch(({ response }) => {
                  this.inProgress = false;
                  this.errors = response.data.errors;
                });
      }
    }
  };
</script>
