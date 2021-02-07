import { SET_FILM, SET_FILMS } from './actions';

export const initialState = {
}

const filmReducer = function (state = initialState, action) {
  switch (action.type) {
    case SET_FILM:
      return {
        ...state,
        detail: action.payload.detail,
      }
    case SET_FILMS:
      return {
        ...state,
        list: action.payload.list,
      }
    default:
      return state;
  }
}

export default filmReducer;
