import Vue from "vue";
import {
    FavoriteService,
    CategoriesService
} from "@/common/api.service";
import {
    FETCH_FAVORITE,
    FAVORITE_PUBLISH,
    FETCH_CATEGORIES
} from "./actions.type";
import {
    SET_FAVORITE,
    SET_CATEGORIES
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
    }
};

export const mutations = {
    [SET_FAVORITE](state, favorite) {
        state.favorite = favorite;
    },
    [SET_CATEGORIES](state, categories) {
        state.favorite.categories = categories;
    },
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
