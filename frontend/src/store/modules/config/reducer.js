import { SET_GOOGLE_CLIENT_ID } from './actions';

export const initialState = {
  googleClientId: undefined,
}

const configReducer = function (state = initialState, action) {
  switch (action.type) {
    case SET_GOOGLE_CLIENT_ID:
      return {
        googleClientId: action.payload,
      }
    default:
      return state;
  }
}

export default configReducer;
