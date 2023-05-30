
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Luke
 */
public class Archive {

    private String ID;
    private String name;

    public Archive(String ID, String name) {
        this.ID = ID;
        this.name = name;
    }

    @Override
    public boolean equals(Object compared) {
        if(this == compared) {
            return true;
        }
        if (!(compared instanceof Archive)) {
            return false;
        }
        Archive comparedArchive = (Archive) compared;

        if (this.ID.equals(comparedArchive.ID)) {
            return true;
        } return false;
    }


    public String getID() {
        return ID;
    }
    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return (this.ID + ": " + this.name);

    }

}
