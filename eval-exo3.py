from fastapi import HTTPException

@app.patch("/books/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):
    #on recupere le livre dans la bdd
    book = bdd.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Livre pas trouvé (il existe pas)")
    
    #on met a jotu les champs fournis
    update_data = book_update.dict(exclude_unset=True)
    
    # on verifie que l'isbn a bien été modifié
    if "isbn" in update_data:
        for b_id, b in bdd.items():
            if b_id != book_id and b["isbn"] == update_data["isbn"]:
                raise HTTPException(status_code=400, detail="ISBN déjà utilisé")
    
    #mise a jour du=livre en bdd puis on return book
    book.update(update_data)
    
    return book