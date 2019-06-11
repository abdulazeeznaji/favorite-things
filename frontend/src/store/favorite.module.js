import Vue from "vue";
import {
  FavoriteService,
} from "@/common/api.service";
import {
  FETCH_FAVORITE,
  FAVORITE_PUBLISH,
} from "./actions.type";
import {
  SET_FAVORITE,
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
    category: '',
    created_date: curday('-')
  },
};

export const state = { ...initialState };

export const actions = {
  [FAVORITE_PUBLISH]({ state }) {
    return FavoriteService.create(state.favorite);
  }
};

export const mutations = {
  [SET_FAVORITE](state, favorite) {
    state.favorite = favorite;
  }
};

const getters = {
  favorite(state) {
    return state.favorite;
  }
};

export default {
  state,
  actions,
  mutations,
  getters
};
