import Vue from "vue";
import {
    FavoriteService,
    CategoriesService
} from "@/common/api.service";
import {
    FAVORITE_DELETE,
    FAVORITE_PUBLISH,
    FETCH_CATEGORIES,
    FETCH_FAVORITE,
    FAVORITE_RESET_STATE,
    FAVORITE_EDIT
} from "./actions.type";
import {
    SET_FAVORITE,
    SET_CATEGORIES,
    RESET_STATE
} from "./mutations.type";

var curday = function(sp){
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //As January is 0.
    var yyyy = today.getFullYear();

    if(dd<10) dd='0'+dd;
    if(mm<10) mm='0'+mm;
    return (mm+sp+dd+sp+yyyy);
};

const initialState = {
    favorite: {
        title: "",
        description: "",
        ranking: '',
        categories: [],
        created_date: curday('-'),
        selected:''
    }
};

export const state = { ...initialState };

export const actions = {
    [FAVORITE_PUBLISH]({ state }) {
        return FavoriteService.create(state.favorite);
    },
    [FETCH_CATEGORIES](context) {
        return CategoriesService.get()
            .then(({ data }) => {
                context.commit(SET_CATEGORIES, data.categories);
            })
            .catch(error => {
                throw new Error(error);
            });
    },
    [FAVORITE_DELETE](context, id) {
        return FavoriteService.destroy(id);
    },
      [FAVORITE_EDIT]({ state }) {
        console.log(state.favorite)
    return FavoriteService.update(state.favorite.id, state.favorite);
  },
    async [FETCH_FAVORITE](context, favoriteSlug, prevFavorite) {
        if (prevFavorite !== undefined) {
            return context.commit(SET_FAVORITE, prevFavorite);
        }
        const { data } = await FavoriteService.get(favoriteSlug);
        context.commit(SET_FAVORITE, data.favorite);
        return data;
    },
    [FAVORITE_RESET_STATE]({ commit }) {
        commit(RESET_STATE);
    }

};

export const mutations = {
    [SET_FAVORITE](state, favorite) {
        state.favorite = favorite;
    },
    [SET_CATEGORIES](state, categories) {
        state.favorite.categories = categories;
    },
    [RESET_STATE]() {
        for (let f in state) {
            Vue.set(state, f, initialState[f]);
        }
    }
};

const getters = {
    favorite(state) {
        return state.favorite;
    },
    categories(state) {
        return state.categories;
    },
    selected(state) {
        return state.selected;
    }
};

export default {
    state,
    actions,
    mutations,
    getters
};
