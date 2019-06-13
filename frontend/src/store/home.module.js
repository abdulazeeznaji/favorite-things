import { FavoriteService } from "@/common/api.service";
import { FETCH_FAVORITES } from "./actions.type";
import {
  FETCH_START,
  FETCH_END,
} from "./mutations.type";

const state = {
  favorites: [],
  isLoading: true,
};

const getters = {
  favorites(state) {
    return state.favorites;
  },
  isLoading(state) {
    return state.isLoading;
  }
};

const actions = {
  [FETCH_FAVORITES]({ commit }, params) {
    commit(FETCH_START);
    return FavoriteService.query(params.type, params.filters)
      .then(({ data }) => {
        commit(FETCH_END, data);
      })
      .catch(error => {
        throw new Error(error);
      });
  }
};

const mutations = {
  [FETCH_START](state) {
    state.isLoading = true;
  },
  [FETCH_END](state, { favorites }) {
      state.favorites = favorites;
    state.isLoading = false;
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
