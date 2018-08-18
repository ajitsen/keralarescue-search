import React, { PropTypes }  from 'react';
import classNames from 'classnames';

/*
 * A component implementing a simple results list.
 *
 * props are:
 *  results: an array of objects holding data for each result
 */

const Results = ({searchResults, highlighting}) => {

    function get_hl_or_normal_title(hit) {
        let title = (highlighting &&
            highlighting[hit.id] && highlighting[hit.id].name) ?
            highlighting[hit.id].name.join("") : "";
        if (title === "") {
            title = hit.name || "product id " + hit.id;
        }
        if (hit.url) {
            return "<a target='_blank' href=\""+hit.url+"\">"+title+"</a><span>"+
                (hit.link_type_s === "video"? "&nbsp; ▶️":"") + "</span>";
        }
        return title;
    }

    function get_hl_or_normal_ingred(hit) {
      let ingredients = hit.main_ingred;
      if (highlighting && highlighting[hit.id] && highlighting[hit.id].main_ingred) {
        ingredients = highlighting[hit.id].main_ingred;
      }

      if (ingredients && ingredients instanceof Array) {
          const count = ingredients.length;
          let ing_spans = "";
          ingredients.map((ing, i) => {
              ing_spans += ing;
              if (i+1 < count) {
                  ing_spans += ", ";
              }
          });
          return ing_spans;
      }
      return hit.main_ingred;
    }

    function get_notes(hit) {
        if (hit.notes_t && /\S/.test(hit.notes_t)) {
            return <div className="app_normal"><em>🗒 </em>{hit.notes_t}</div>
        }
        return '';
    }

    function get_dish_type(hit) {
        if (hit.dish_type_s && /\S/.test(hit.dish_type_s)) {
            return <span className="app_capitalize"><em>🍽</em>{hit.dish_type_s}&nbsp;&nbsp;</span>
        }
        return '';
    }

    function get_utensils(hit) {
        let utensils = hit.microwave_b ? ' Microwave' : '';
        if (hit.blender_b) {
            if (utensils !== '') {
                utensils += ' |';
            }
            utensils += ' Blender';
        }
        if (hit.oven_b) {
            if (utensils !== '') {
                utensils += ' |';
            }
            utensils += ' Oven';
        }
        if (utensils !== '') {
            utensils = <span>Utensil: {utensils}&nbsp;&nbsp;</span>
        }
        return utensils;
    }

    const results = searchResults.map((hit) => {
      const titleHtml = { __html: get_hl_or_normal_title(hit) };
      const ingredientsHtml =  { __html: '<span>Main Ingredients: </span>' + get_hl_or_normal_ingred(hit) };

      const ingClassNames = classNames({"app_vsp03":true, "app_capitalize":true, "app_content": true});
      const prepTime = hit.prep_time_i ?  <em>⏱ {hit.prep_time_i} m&nbsp;&nbsp;</em>:"";
      const utensils = get_utensils(hit);
      const dishType = get_dish_type(hit);
      const notes = get_notes(hit);

      return <div key={hit.id} className="app_hit">
        <h4 className={"app_title"} dangerouslySetInnerHTML={titleHtml} />
        <div className={ingClassNames} dangerouslySetInnerHTML={ingredientsHtml} />
        {notes}
        <div className="text-muted app_vsp03">
          {prepTime}
          {utensils}
          {dishType}
        </div>
      </div>;
    });

  return <div className="col-sm-8">
    {results}
  </div>;
};

Results.propTypes = {
  searchResults: PropTypes.arrayOf(PropTypes.object).isRequired,
  highlighting: PropTypes.object
};

export default Results;
